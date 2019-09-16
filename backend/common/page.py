# coding:utf-8
# @Time  : 2019-09-02 19:48
# @Author: Xiawang
# Description:


class Page:
    def get_total_page_count(self, total_count=0, per_page=10):
        if total_count / per_page > 1:
            total_page_count = int(total_count / per_page) + 1
        elif 0 < int(total_count / per_page) < 1:
            total_page_count = 1
        else:
            total_page_count = 0
        return total_page_count

    def is_has_next_page(self, pageNo, total_page_count):
        if pageNo == 1 and total_page_count - pageNo >= 1:
            has_next_page = True
        elif total_page_count - pageNo >= 1:
            has_next_page = True
        elif total_page_count - pageNo == 0:
            has_next_page = False
        else:
            has_next_page = False
        return has_next_page

    def is_has_previous_page(self, pageNo, total_page_count):
        if pageNo == 1:
            has_previous_page = False
        elif total_page_count - pageNo <= 0:
            has_previous_page = True
        else:
            has_previous_page = False
        return has_previous_page

    def verify_previous_page_and_next_page(self, pageNo, total_page_count):
        return self.is_has_next_page(pageNo, total_page_count), self.is_has_previous_page(pageNo, total_page_count)

    def pagination(self, currentPageNo, hasNextPage, hasPreviousPage, totalCount, totalPageCount):
        pagination_result = {
            'currentPageNo': currentPageNo,
            'hasNextPage': hasNextPage,
            'hasPreviousPage': hasPreviousPage,
            'totalCount': totalCount,
            'totalPageCount': totalPageCount
        }
        return pagination_result
