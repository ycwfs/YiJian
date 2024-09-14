# -*- coding: utf-8 -*-
# Copyright 2024 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from datasets import Dataset

from yijian_community.model.base_infer import Infer
from yijian_community.utils.util_func import console


class APIInfer(Infer):

    def __init__(self, model_name: str):
        super().__init__(model_name)
        # console.log(
        #     "This class will be implemented in the next update or you are welcomed to make a contribution."
        # )
        # self.model_name = model_name
        # self.infer = None

    def infer_data(self, data: str):
        # console.log(
        #     "This will be implemented in the next update or you are welcomed to make a contribution."
        # )
        pass

    def infer_dataset(self, dataset: Dataset) -> Dataset:
        # console.log(
        #     "This will be implemented in the next update or you are welcomed to make a contribution."
        # )
        pass

class OpenAITxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://github.com/openai/openai-python")

    def call_gpt_vision_api(self, api_key,
                            system_prompt,
                            user_prompt,
                            models=['gpt-4o-mini','gpt-4o-mini-0718']):
        api_url = 'https://api.gptsapi.net/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        data = {
            "model": random.choices(models,weights=[0.5,0.5])[0],
            "messages": [
                {"role": "system", "content":f"{system_prompt}"},
                {"role": "user", "content": f"{user_prompt}"}
            ],
            #"max_tokens": 500
        }

        try:
            response = requests.post(api_url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()

            #print(result)
            if 'choices' in result and result['choices']:
                return result['choices'][0]['message']['content']
            else:
                print('No results returned from the API, return None.')
                return None

        except requests.exceptions.HTTPError as errh:
            if errh.response.status_code == 401:
                print('Invalid API key provided.')
            elif errh.response.status_code == 429:
                print(
                    'API request limit has been reached. Please try again later.')
            else:
                print(f'HTTP error occurred: {errh}')
        except requests.exceptions.ConnectionError:
            print('Network error occurred. Please check your connection.')
        except requests.exceptions.Timeout:
            print('The request timed out. Please try again later.')
        except requests.exceptions.RequestException as err:
            print(f'An error occurred: {err}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

        print('API request failed, return None.')
        return None

    def call_gpt_vision_api_with_retry(self, api_key, system_prompt, user_prompt, max_retries=50, initial_delay=1, max_delay=60):
        for attempt in range(max_retries):
            try:
                result = call_gpt_vision_api(api_key, system_prompt, user_prompt)
                if result is not None:
                    return result
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
            
            if attempt < max_retries - 1:
                delay = min(initial_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
                print(f"Retrying in {delay:.2f} seconds...")
                time.sleep(delay)
        
        print(f"All {max_retries} attempts failed. Returning None.")
        return None

    def infer_data(self, data, system_prompt, user_prompt) -> str:
        return call_gpt_vision_api_with_retry(self, api_key, system_prompt, user_prompt)

    def infer_dataset(self, dataset: Dataset, system_prompt, user_prompt, target_column: str = "prompt_text") -> Dataset:
        
        response_texts = []
        for d in dataset:
            response_texts.append(infer_data(d[target_column], system_prompt, user_prompt))

        return dataset.add_column("response_text", response_texts)

class AnthropicTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://github.com/anthropics/anthropic-sdk-python")


class CohereTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://github.com/cohere-ai/cohere-python")


class TongyiQwenTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log(
            "Reference: https://help.aliyun.com/zh/dashscope/developer-reference/api-details"
        )


class MoonshotTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://platform.moonshot.cn/docs/api/chat#基本信息")


class BaichuanTxt2TxtInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://platform.baichuan-ai.com/docs/api")


class StabilityAITxt2ImgInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://platform.stability.ai/docs/api-reference")


class OpenAITxt2ImgInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log("Reference: https://platform.openai.com/docs/guides/images")


class MidJourneyTxt2ImgInfer(APIInfer):

    def __init__(self, model_path: str):
        super().__init__(model_path)
        console.log(
            "Reference: https://docs.midjourney.com/docs/quick-start or https://github.com/erictik/midjourney-api"
        )
