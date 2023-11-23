from json import dumps

class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __default__(obj: "Parser"):
        return {
            **{
                attr: (
                    getattr(obj, attr)
                )
                for attr in obj.__dict__
                if getattr(obj, attr) is not None and not attr.startswith("_")
            }
        } if not isinstance(obj, set) else [i for i in obj]

    def __str__(self) -> str:
        return dumps(self, default=Parser.__default__, indent=2)