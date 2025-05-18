class PageInfo:
    """
    分页信息
    """
    page: int
    size: int
    total: int
    data: list

    def __init__(self, page: int, size: int, total: int, data: list):
        self.page = page
        self.size = size
        self.total = total
        self.data = data
