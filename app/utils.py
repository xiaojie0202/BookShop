from django.core.paginator import Paginator


# 分页专用
class CustomPaginator(Paginator):

    def __init__(self, current_page, per_pager_num, *args, **kwargs):
        '''
        :param current_page: 当前页
        :param per_pager_num: 总共需要显示几页
        '''
        self.current_page = int(current_page)
        self.per_pager_num = int(per_pager_num)
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def pager_num_range(self):
        '''
        :return: 返回一个列表，页面显示这些页码
        '''
        if self.num_pages < self.per_pager_num:
            return range(1, self.num_pages + 1)
        part = int(self.per_pager_num / 2)
        if self.current_page <= part:
            return range(1, self.per_pager_num + 1)
        if (self.current_page + part) > self.num_pages:
            return range(
                self.num_pages -
                self.per_pager_num +
                1,
                self.num_pages +
                1)
        return range(self.current_page - part, self.current_page + part + 1)

