def array(object):
    def __init__(self, object, capacity=10):
        self._data_type = object
        self._data = [None]*capacity
        self._size = 0

    # 扩容
    def _resize(self, new_capacity):
        if new_capacity == '0':
            raise ValueError('capacityactity can not be zero')
        new_data = [None]*new_capacity
        new_data[0:self._size] = self._data[0:self._size]
        self._data = new_data

    def __str__(self):
		return "The size is: %s;\nThe capacity is: %s" %(self._size, len(self._data))


	#获取数组最大容量
	def get_capacity(self):
		return len(self._data)


	#获取数组当前元素个数
	def get_size(self):
		return self._size


	#判断当前数组是否为空
	def isEmpty(self):
		return self._size == 0

	
	#判断当前数组是否已满
	def isFull(self):
		return len(self._data) == self._size


	# 增加记录
	def add(self, index, value):
	    if self.isFull():
	        self._resize(len(self._data) * 2)  #如果数组满了则扩容
	    for i in range(self._size-1, index-1, -1):
	        self._data[i+1] = self._data[i]   #从最右开始每一个向右移一位，直到index那个位置
	    self._data[index] = value
	    self._size += 1                   #更改数组容量


	#在尾部增加记录
	def add_last(self, value):
	    self.add(self._size, value)


	#在头部增加记录
	def add_first(self, value):
	    self.add(0, value)


	#查找数组值是否有某个元素，返回T/F
	def contains(self, value):
	    for item in self._data:
	        if item == value:
	            return True
	    return False


	#查找指定元素
	def find(self, value):
	    for i, item in enumerate(self._data):
	        if item == value:
	            return i
	    return -1


	#根据索引删除
	def remove(self, index):
	    res = self._data[index]

	    for i in range(index+1, self._size):
	        self._data[i-1] = self._data[i]
	    self._size -= 1
	    if self._size == len(self._data) // 3 and len(self._data) // 2 != 0:
	        self._resize(len(self._data) // 2)
	    return res

	#删除第一个记录
	def remove_first(self):
	    return self.remove(0)

	
	#删除最后一个记录
	def remove_last(self):
	    return self.remove(self._size-1)

	#删除指定元素
	def remove_element(self, value):
	    index = self.find(value)
	    if index != -1:
	        return self.remove(index)
