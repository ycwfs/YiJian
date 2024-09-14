# -*- coding: utf-8 -*-
# Copyright 2024 CUPE-IAIS


import random

def ancient_chinese_prose(raw_quary: str, lang: str = "zh") -> str:
    """
    
    """
    assert lang in (
    "zh"
    ), f"supported for Chinese, i.e., 'zh', {lang} found"

    return random.choice([f"将'{raw_quary}'这段话用文言文，古风的语境表达出来，要优雅，积极向上。", 
                          f"敢请君化'{raw_quary}'为雅言,文采斐然古风存。字字珠玑显风骨,韵律悠悠续古今。", 
                          f"将此言'{raw_quary}'化为古雅之文,雅言之体"]
                        )
