def ft_count_harvest_recursive() -> None:
    target = int(input("Days until harvest: "))

    def recursive(nb: int = 1) -> None:
        if (nb <= target):
            print(f"Day {nb}")
            recursive(nb + 1)
        else:
            print("Harvest time!")
    recursive()
