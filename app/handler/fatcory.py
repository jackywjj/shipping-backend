from datetime import datetime


class ResponseFactory:
    """
    格式化
    """

    @staticmethod
    def model_to_dict(obj, *ignore: str):
        if obj is None:
            return None
        data = dict()
        for c in obj.__table__.columns:
            if c.name in ignore:
                continue
            val = getattr(obj, c.name)
            if isinstance(val, datetime):
                data[c.name] = val.strftime("%Y-%m-%d %H:%M:%S")
            else:
                data[c.name] = val
        return data

    @staticmethod
    def model_to_list(data: list, *ignore: str):
        return [ResponseFactory.model_to_dict(x, *ignore) for x in data]

    @staticmethod
    def to_dict(obj, *sub_list: dict):
        """
        将 SQLAlchemy 模型及其子列表转换为字典
        """
        data = ResponseFactory.model_to_dict(obj)
        for sub in sub_list:
            for item in sub.items():
                if isinstance(item[1], list):
                    data[item[0]] = ResponseFactory.model_to_list(item[1])
                else:
                    data[item[0]] = ResponseFactory.model_to_dict(item[1])
        return data
