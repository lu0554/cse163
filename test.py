import matplotlib.pyplot as plt

income = [20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
depression_status = [0, 1, 1, 0, 1, 1, 0, 0, 1]

plt.hist(income, bins=3, color='green', alpha=0.5, label='Non-depressed')
plt.hist([income[i] for i in range(len(depression_status)) if depression_status[i] == 1], bins=3, color='red', alpha=0.5, label='Depressed')
plt.title('Income Distribution by Depression Status')
plt.xlabel('Income')
plt.ylabel('Count')
plt.legend()
plt.show()
plt.savefig("abc.png")