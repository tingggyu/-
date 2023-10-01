from collections import defaultdict


class Lexeme:
    """處理 lexeme 資料"""

    def __init__(self, lexeme_list: list, lexeme_data: dict):
        self.lexeme_list = lexeme_list
        self.lexeme_data = lexeme_data

    def _get_data(self, processed_data: dict, raw_data: dict = None) -> dict:
        """將 proecssed data 中的資料和 raw data 中的資料連接起來

        processed_data (dict): 處理過的資料
        raw_data (dict): 要處理的資料
        """

        audio_col = ",".join(
            [processed_data['audio_name'], raw_data['audio_name'] if raw_data else "--"]
        )

        attr_col = ",".join(
            [processed_data['attribute'], raw_data['attribute'] if raw_data else "--"]
        )

        tone_col = ",".join(
            [processed_data['tone_pitch'], raw_data['tone_pitch'] if raw_data else "--"]
        )

        data = {
            "audio_name": audio_col,
            "attribute": attr_col,
            "tone_pitch": tone_col,
        }

        return data

    def _concat_lexeme(self, processed_data: list, raw_data: list) -> list:
        """根據腔調組合不同的拼音資料"""

        tmp = []

        for n_data in processed_data:
            for data in raw_data:
                tmp.append(self._get_data(n_data, data))

        return tmp

    def _concat_lexeme_with_not_exist_accent(self, processed_data: list) -> list:
        tmp = []

        for n_data in processed_data:
            tmp.append(self._get_data(n_data))

        return tmp

    def concat_lexeme(self) -> dict:
        """生成根據不同的腔調組合起來的拼音資料"""

        processed_data = self.lexeme_data[self.lexeme_list[0]]

        result = defaultdict(list)

        for i in range(1, len(self.lexeme_list)):
            for accent in processed_data:
                processed_accent_data = processed_data[accent]
                accent_data = self.lexeme_data[self.lexeme_list[i]].get(accent)

                if accent_data is None:
                    data = self._concat_lexeme_with_not_exist_accent(processed_accent_data)

                else:
                    data = self._concat_lexeme(processed_accent_data, accent_data)

                result[accent] = data

            processed_data = result

        return result

    def _process_concat_data(self, data: dict) -> dict:
        """處理轉換完的資料，例如將名字加上連接符號、將字串轉為 list"""

        result = {}

        # 姓名為三個字
        name = data["attribute"].split(",")
        if len(name) == 3:
            d_name = f"{name[0]},{'-'.join(name[1:])}"

        # 兩個字
        elif len(name) == 2:
            d_name = f"{name[0]},{name[1]}"

        else:
            d_name = f"{name[0]}{name[1]},{'-'.join(name[2:])}"

        d_tone = data["tone_pitch"].replace(",", " ")

        result["attribute"] = d_name
        result["tone_pitch"] = d_tone
        result["audio_name"] = data["audio_name"]

        return result

    def process_concat_data(self, data: dict) -> list:
        """生成最後可以顯示在網頁上的資料

        data (dict): 由 `concat_lexeme` 生成的資料

        """

        result = list()

        for tone in data:
            for d in data[tone]:
                process_result = self._process_concat_data(d)
                process_result["accent"] = tone

                result.append(process_result)

        return result
