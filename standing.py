import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100) # years

start_x = np.arange(20).reshape((1, 1, -1)).repeat(3, axis=0).repeat(3, axis=1)
end_x = np.arange(80).reshape((1, 1, -1)).repeat(3, axis=0).repeat(3, axis=1)

start_stats = np.array([8.5, 0, 20]).reshape(1, 3, 1)
end_stats = np.array([[8.5, 4, 11.5], [8.5, 8, 7.5], [8.5, 12, 3.5]]).reshape(3, 3, 1)
assert np.all(end_stats.sum(axis=1) == 24)

start_y = start_x * start_stats
end_y = (end_x * end_stats) + start_y[:, :, -1:]

x = np.concatenate((start_x, end_x+19), axis=2)
y = np.concatenate((start_y, end_y), axis=2)

pessimistic = 0
realistic = 1
optimistic = 2

sleep_hours = [8.5, 8.5, 8.5]
stand_hours = [4, 6, 8]
sit_hours = [24 - sleep_hours[pessimistic] - stand_hours[pessimistic], 24 - sleep_hours[realistic] - stand_hours[realistic], 24 - sleep_hours[optimistic] - stand_hours[optimistic]]

# fig, (ap, ar, ao) = plt.subplots(1, 3)
fig, axes = plt.subplots(1, 3, sharey=True, constrained_layout=True)
print(axes)

for i, (case_xs, case_ys) in enumerate(zip(x, y)):
    for label, case_x, case_y in zip(['hours spent sleeping', 'hours spent standing', 'hours spent sitting'], case_xs, case_ys):
        axes[i].plot(case_x, case_y, label=label)

    axes[i].legend()
    axes[i].set_xlabel('years')
    axes[i].set_ylabel('hours')

plt.show()
