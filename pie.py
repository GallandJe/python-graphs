import matplotlib.pyplot as plt

labels = 'Python', 'Ruby', 'PHP', 'Node.js'
sizes = [1000,2000,3000,4000]
colors = ['blue', 'red', 'purple', 'green']

plt.pie(sizes, labels=labels, colors=colors)
plt.title("Number of programmers by language")
plt.show()
