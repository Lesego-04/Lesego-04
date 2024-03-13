import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import datetime



current_month = datetime.datetime.now().strftime('%B')
categories = ["Clothes", "Food", "Travel", "spoils"]

def add_entry(month, salary, **expenses):
    with open("finance_data_data_monthly.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([month, salary] + [expenses[category] for category in categories])




def animate(i, bars, values):
    progress = i / 50
    for bar, value in zip(bars, values):
        bar.set_height(value * progress)


def visualize_finances(salary):
    expenses_data = {}

    for category in categories:
        expense = float(input(f'Expenses for {category} in {current_month}: '))
        expenses_data[category] = expense

    total_expenses = sum(expenses_data.values())

    add_entry(current_month, salary, **expenses_data)

    labels = categories + ['Total salary', 'Total expenses', 'Net savings']
    values = list(expenses_data.values())+ [salary, total_expenses, salary - total_expenses]

    category_colors = ['#FF0000', '#00FF00', '#000000', '#7FFFD4']

    summary_colors = ['red', 'black', 'green']
    
    colors = category_colors + summary_colors

    fig, ax = plt.subplots(figsize=(18, 9))

    bars = ax.bar(labels, [0] * len(labels), color = colors)

    ax.set_ylim(0, max(values) * 1.2)

    ax.set_xlabel('Categories', fontsize = 14, fontweight = 'bold')

    ax.set_ylabel('Amount', fontsize =14, fontweight= 'bold')

    ax.set_title(f'Financial Overview for {current_month} - Generated on {datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%s %p")}',
    fontsize =16 , fontweight = 'bold')
    ani = animation.FuncAnimation(fig, animate, frames=50, fargs=[bars, values], repeat=False)
    expense_legend = ax.legend(handles=bars[:4], labels= categories, title="Expensee Categories", loc= 'upper left', 
                                 bbox_to_anchor=(1.03, 1))
    ax.add_artist(expense_legend)

    summary_labels = ['Total Salary', 'Total Expenses', 'Net Savings']

    summary_legend = ax.legend(handles=bars[4:], labels=summary_labels, title="Financial Summary", loc="upper left",
                                 bbox_to_anchor=(1.03, 0.75))
    
    ax.grid(axis='y', linestyle='--', alpha=0.7, color= 'grey')
    writergif = animation.PillowWriter(fps=70)
    ani.save('filename.gif',writer=writergif)

    plt.tight_layout()

    plt.subplots_adjust(right = 0.83, left = 0.1)

    mng = plt.get_current_fig_manager()
    # mng.window.state('zoomed')
    # plt.get_current_fig_manager().window.showMaximized()

plt.show()

salary = float(input(f'salary for {current_month}: '))
plt.figure(figsize=(18, 9))
visualize_finances(salary)


# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# sns.distplot([0,1,2,4,5])

# plt.show()

# xpoints = np.array([0, 6])
# ypoints = np.array([0,250])

# plt.plot(xpoints, ypoints)
# plt.show()











