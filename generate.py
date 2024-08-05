import pandas as pd
import matplotlib.pyplot as plt

# 模块数据
data_modules = {
    "Module 8": {
        "Time": [10, 20, 30, 40, 50, 60],
        "Threads": [8] * 6,
        "TPS": [30841.33, 12954.21, 4818.79, 3644.43, 6082.37, 6734.70],
        "QPS": [30841.33, 12954.21, 4818.79, 3644.43, 6082.37, 6734.70],
        "95% Latency (ms)": [0.19, 0.77, 14.73, 16.41, 13.22, 12.75]
    },
    "Module 16": {
        "Time": [10, 20, 30, 40, 50, 60],
        "Threads": [16] * 6,
        "TPS": [87007.10, 55205.31, 38658.40, 38691.70, 41753.19, 38849.07],
        "QPS": [87007.10, 55205.31, 38658.40, 38691.70, 41753.19, 38849.07],
        "95% Latency (ms)": [0.22, 0.26, 0.31, 0.33, 0.29, 0.34]
    },
    "Module 32": {
        "Time": [10, 20, 30, 40, 50, 60],
        "Threads": [32] * 6,
        "TPS": [149602.90, 80359.08, 68105.55, 84401.11, 91819.84, 80138.85],
        "QPS": [149602.90, 80359.08, 68105.55, 84401.11, 91819.84, 80138.85],
        "95% Latency (ms)": [0.42, 0.46, 0.53, 0.42, 0.39, 0.42]
    },
    "Module 64": {
        "Time": [10, 20, 30, 40, 50, 60],
        "Threads": [64] * 6,
        "TPS": [90576.56, 90959.48, 114170.40, 115053.90, 137982.12, 112693.66],
        "QPS": [90576.56, 90959.48, 114170.40, 115054.00, 137982.02, 112693.66],
        "95% Latency (ms)": [1.25, 1.14, 1.03, 0.97, 0.89, 0.86]
    },
    "Module 128": {
        "Time": [10, 20, 30, 40, 50, 60],
        "Threads": [128] * 6,
        "TPS": [158240.29, 129469.09, 120345.60, 119647.31, 106505.81, 140405.29],
        "QPS": [158240.29, 129469.09, 120345.60, 119647.31, 106505.81, 140405.29],
        "95% Latency (ms)": [1.73, 2.00, 3.68, 3.55, 3.96, 2.48]
    },
    "Module 256": {
        "Time": [10, 20, 30, 40, 50, 60],
        "Threads": [256] * 6,
        "TPS": [110122.68, 93278.08, 109444.12, 117405.25, 122018.31, 124087.13],
        "QPS": [110122.68, 93278.08, 109444.02, 117405.35, 122018.31, 124087.13],
        "95% Latency (ms)": [14.46, 14.21, 10.46, 10.09, 9.91, 9.73]
    },
    "Module 512": {
        "Time": [10, 20, 30, 40, 50, 60],
        "Threads": [512] * 6,
        "TPS": [118892.41, 110699.71, 115817.93, 116131.80, 121413.02, 131577.30],
        "QPS": [118892.41, 110699.71, 115817.93, 116131.80, 121413.02, 131577.30],
        "95% Latency (ms)": [30.26, 32.53, 29.19, 29.19, 27.17, 25.74]
    }
}

# 计算每个模块的指标
def calculate_metrics(data):
    results = []
    for module_name, data_module in data.items():
        df = pd.DataFrame(data_module)
        average_qps = df['QPS'].mean()
        average_tps = df['TPS'].mean()
        latency_95 = df['95% Latency (ms)'].iloc[-1]  # 取最后一个值作为 95% 延迟

        results.append({
            'Module': module_name,
            'Threads': df['Threads'][0],  # 使用相同的 Threads 值
            'QPS': average_qps,
            'TPS': average_tps,
            '95% latency (ms)': latency_95,
            'Minimum Latency': df['95% Latency (ms)'].min(),
            'Average Latency': df['95% Latency (ms)'].mean(),
            'Maximum Latency': df['95% Latency (ms)'].max(),
            'Total Latency Sum': df['95% Latency (ms)'].sum()
        })
    return pd.DataFrame(results)

# 计算并输出结果
df_results = calculate_metrics(data_modules)

# 输出到文件
output_file = 'point_select.csv'
df_results.to_csv(output_file, index=False, encoding='utf-8-sig')  # 保存为 CSV 文件
print(f"结果已输出到文件: {output_file}")

# 打印结果
print(df_results)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(df_results['Threads'], df_results['QPS'], marker='o', label='Average QPS')
plt.title('Threads vs Average QPS')
plt.xlabel('Threads')
plt.ylabel('Average QPS')
plt.xticks(df_results['Threads'])  # 设置 x 轴刻度
plt.grid()
plt.legend()
plt.savefig('threads_vs_average_qps.png')  # 保存图表为图片
plt.show()  # 显示图表
