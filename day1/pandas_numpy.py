import pandas as pd
import numpy as np

# 构造一个小表格
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Score': [88, 92, 95, 70, 85]
}
df = pd.DataFrame(data)

# 统计平均分
print("Average score:", df['Score'].mean())

# 找出分数大于 90 的学生
print("Students with score > 90:")
print(df[df['Score'] > 90])

# 增加一列随机加分
df['Bonus'] = np.random.randint(0, 10, size=len(df))
print(df)
