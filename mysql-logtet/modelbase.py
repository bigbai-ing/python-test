import datetime

sql_time_format = "%Y-%m-%d %H:%M:%S"

def format_time(src_time, src_time_fmt, date_time_obj=False):
    '''
    对底层返回的时间进行不同的格式转换
    ：param src_time: iass层返回的时间
    ：param src_time_fmt：iass层返回的时间格式
    ：param date_time_obj: 是否需要返回结果为 datetime对象
    ：return： 返回时间戳或者datetime对象
    '''
    tmp_time = src_time
    if isinstance(tmp_time, datetime):
	tmp_time = src_time.strftime(src_time_fmt)
    dst_time = datetime.strptime(tmp_time, src_time_fmt)
    return dst_time if date_time_obj else int(dst_time.timestamp())


class ModelBase:
    def to_dict(self, placeholder_column=None, need_params=None):
	if need_params:
	    keys = need_params
	elif hasattr(self, "__mapper__"):
	    keys = [prop.key for prop in self.__mapper__.iterate_properties]
	else:
	    keys = list(vars(self).keys())
	if placeholder_column:
	    keys.remove(placeholder_column)
	format_data = {}
	for key in keys:
	    format_data[key] = getattr(self, key)
	    if isinstance(format_data[key], datetime.datetime):
		format_data[key] = format_time(format_date[key], sql_time_format)
	return format_data
