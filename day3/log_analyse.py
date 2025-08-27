import pandas as pd

ZH_LOG_PATH="/Users/wangjian/work/logs/zh.csv"
EN_LOG_PATH="/Users/wangjian/work/logs/en.csv"
pd.set_option("display.max_colwidth", None)  # 不截断 message
pd.set_option("display.max_rows", None)


def get_top_messages(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    # 防御性处理：确保是字符串，避免 None/数字等导致报错或合并异常
    df = df.copy()
    df["Message"] = df["Message"].astype(str)

    parts = []
    # dropna=False 确保 service 为 NaN 的也会被统计到
    for svc, g in df.groupby("Service", dropna=False):
        vc = g["Message"].value_counts(dropna=False).head(top_n)
        tmp = vc.rename("count").reset_index().rename(columns={"index": "Message"})
        # 插入 service 列到最前
        tmp.insert(0, "Service", svc)
        # 按你的要求重排列顺序：service, count, message
        tmp = tmp[["Service", "count", "Message"]]
        parts.append(tmp)

    out = pd.concat(parts, ignore_index=True)
    # 让同一 service 内部按 count 降序展示
    out = out.sort_values(["Service", "count"], ascending=[True, False], ignore_index=True)
    return out

def print_left_aligned(df: pd.DataFrame, max_rows: int):
    # 复制并全部转成字符串，避免默认数值右对齐
    df2 = df.copy().astype(str)
    if max_rows is not None:
        df2 = df2.head(max_rows)

    cols = list(df2.columns)
    # 计算每列宽度：列名或该列中最长字符串的最大值
    widths = {c: max(df2[c].map(len).max(), len(str(c))) for c in cols}

    # 打印表头
    header = "  ".join(str(c).ljust(widths[c]) for c in cols)
    sep = "  ".join("-" * widths[c] for c in cols)
    print(header)
    print(sep)

    # 打印每一行
    for _, row in df2.iterrows():
        line = "  ".join(str(row[c]).ljust(widths[c]) for c in cols)
        print(line)

# 使用示例
df = pd.read_csv(EN_LOG_PATH)
top_df = get_top_messages(df, top_n=3)

# 完整打印（不截断 message）
pd.set_option("display.max_colwidth", None)
pd.set_option("display.colheader_justify", "left")  # 表头左对齐
print_left_aligned(top_df,max_rows=1000000)








