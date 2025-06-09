class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}, Storage: {self.storage}"

class ComputerBuilder:
    def set_cpu(self): pass
    def set_gpu(self): pass
    def set_ram(self): pass
    def set_storage(self): pass
    def get_result(self): pass

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel Core i9"

    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"

    def set_ram(self):
        self.computer.ram = "32GB"

    def set_storage(self):
        self.computer.storage = "2TB NVMe SSD"

    def get_result(self):
        return self.computer

class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self):
        self.builder.set_cpu()
        self.builder.set_gpu()
        self.builder.set_ram()
        self.builder.set_storage()
        return self.builder.get_result()


if __name__ == "__main__":
    builder = GamingComputerBuilder()
    director = Director(builder)
    gaming_pc = director.build_computer()

    print("Gaming PC Configuration:")
    print(gaming_pc)
