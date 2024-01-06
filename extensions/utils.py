from . import jalali





def jalali_convertor(date):
    date = str(date)
    return jalali.Gregorian(date).persian_tuple()