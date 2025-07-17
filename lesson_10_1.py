import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy


def bubble_sort_visualization(data):
    """
    Візуалізація сортування бульбашкою.

    :param data: Початкові дані для сортування та візуалізації.
    """
    # Create a copy to avoid modifying the original data
    data_copy = copy.deepcopy(data)
    n = len(data_copy)

    fig, ax = plt.subplots()
    ax.set_title('Bubble Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    # Create bars
    bars = ax.bar(range(n), data_copy, align='edge', color='skyblue', edgecolor='black')

    # Set y-axis limits for better visualization
    ax.set_ylim(0, max(data_copy) * 1.1)

    def update(frame):
        # Perform one pass of bubble sort
        swapped = False
        for i in range(n - frame - 1):
            if data_copy[i] > data_copy[i + 1]:
                data_copy[i], data_copy[i + 1] = data_copy[i + 1], data_copy[i]
                swapped = True

                # Highlight the bars being compared
                bars[i].set_color('red')
                bars[i + 1].set_color('red')
            else:
                # Reset color for non-swapped bars
                bars[i].set_color('skyblue')
                bars[i + 1].set_color('skyblue')

        # Update bar heights
        for bar, h in zip(bars, data_copy):
            bar.set_height(h)

        # Color the sorted portion (rightmost bars) green
        for i in range(n - frame - 1, n):
            bars[i].set_color('green')

        return bars

    # Create animation with proper interval
    anim = animation.FuncAnimation(
        fig, update, frames=n - 1, interval=1000, repeat=False, blit=False
    )

    # Save animation (with proper file extension)
    try:
        anim.save("bubble_sort_animation.gif", writer='pillow', fps=1)
        print("Animation saved as 'bubble_sort_animation.gif'")
    except Exception as e:
        print(f"Could not save animation: {e}")

    # For non-interactive environments, save as static image
    try:
        plt.savefig("bubble_sort_final.png", dpi=300, bbox_inches='tight')
        print("Final result saved as 'bubble_sort_final.png'")
    except Exception as e:
        print(f"Could not save image: {e}")

    # Show plot (this will work in interactive environments)
    try:
        plt.show()
    except Exception as e:
        print(f"Display not available: {e}")

    return anim  # Return animation object to prevent garbage collection


# Приклад використання
if __name__ == "__main__":
    initial_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Initial data: {initial_data}")

    # Keep reference to animation to prevent garbage collection
    animation_obj = bubble_sort_visualization(initial_data)

    print(f"Original data unchanged: {initial_data}")