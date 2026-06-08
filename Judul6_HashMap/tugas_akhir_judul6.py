#Tugas Akhir Judul 6
#Nama  : Thariq Ariq Setiawan
#NPM   : 2515061073
#Kelas : PSD-E

# Mengimplementasikan Hash Map untuk Inventory Minecraft dengan Open Addressing

class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Entry:
    def __init__(self):
        self.item_id = None
        self.item_name = None
        self.quantity = 0
        self.state = SlotState.EMPTY

class MinecraftInventory:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, item_id):
        return item_id % self.SIZE

    def add_item(self, item_id, item_name, quantity):
        idx = self.hash_function(item_id)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].item_id == item_id:
                    self.table[i].quantity += quantity
                    return True

            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].item_id = item_id
                self.table[i].item_name = item_name
                self.table[i].quantity = quantity
                self.table[i].state = SlotState.OCCUPIED
                return True

        return False

    def search_item(self, item_id):
        idx = self.hash_function(item_id)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (
                self.table[i].state == SlotState.OCCUPIED
                and self.table[i].item_id == item_id
            ):
                return self.table[i]

        return None

    def remove_item(self, item_id):
        item = self.search_item(item_id)

        if item is None:
            return False

        item.state = SlotState.DELETED
        return True

    def display_inventory(self):
        print("\n=== INVENTORY MINECRAFT ===")

        for i in range(self.SIZE):
            print(f"Slot {i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("Kosong")

            elif self.table[i].state == SlotState.DELETED:
                print("Item Dihapus")

            else:
                print(
                    f"{self.table[i].item_name} "
                    f"x{self.table[i].quantity}"
                )

def main():
    inventory = MinecraftInventory()

    inventory.add_item(1, "Dirt", 64)
    inventory.add_item(11, "Stone", 32)
    inventory.add_item(21, "Diamond", 5)
    inventory.add_item(2, "Oak Wood", 20)

    inventory.display_inventory()

    item = inventory.search_item(21)

    if item:
        print(
            f"\nItem ditemukan: "
            f"{item.item_name} x{item.quantity}"
        )

    inventory.remove_item(11)

    print("\nSetelah Stone dibuang:")
    inventory.display_inventory()

    item = inventory.search_item(21)

    if item:
        print(
            f"\nDiamond masih ada: "
            f"{item.quantity} buah"
        )

if __name__ == "__main__":
    main()