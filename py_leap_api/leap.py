from .utils import send_and_parse
import warnings


class TryLeap:
    
    def __init__(self, api: str, model: str=None) -> None:
        self.api = api
        self.model = model
        # create endpoints
        self.__endpoint_creator()
        
    def __endpoint_creator(self) -> None:
        version = "v1"
        host = f"https://api.tryleap.ai/api/{version}/images/models"
        
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.api}"
        }
        
        if self.model:
            self.endpoint = {
                "create_model": f"{host}",
                "upload_images_url": f"{host}/{self.model}/samples/url",
                "upload_images": f"{host}/{self.model}/samples",
                "training": f"{host}/{self.model}/queue",
                "generate_image": f"{host}/{self.model}/inferences",
                "output_image": f"{host}/{self.model}/inferences/" + "{inference_id}",
                "output_images": f"{host}/{self.model}/inferences",  
            }
            
        else:
            self.endpoint = {
                "create_model": f"{host}"
            }
            warnings.warn("Warning use method set_model to set the model id.", UserWarning)
            
        
    def set_model(self, model:str) -> None:
        self.model = model
        # recreate endpoints whit model id 
        self.__endpoint_creator()
        
    
    async def create_model(self, title:str, subject:str="@me", identifier:str=None) -> dict:
        payload = {
            "title": title,
            "subjectKeyword": subject,
            "subjectIdentifier": identifier
            }
        
        response = await send_and_parse(
            method="POST",
            url=self.endpoint["create_model"],
            headers=self.headers,
            json=payload
        )
        
        return response.json()
        
    async def upload_images_url(self, images:list, return_object:bool=True) -> dict:
        params = {"returnInObject": return_object}

        if len(images)>20:
            warnings.warn("Warning the API endpoint accepts max 20 images.", UserWarning)

        payload = {"images": images[:20]}

        response = await send_and_parse(
            method="POST",
            url=self.endpoint["upload_images_url"],
            headers=self.headers,
            params=params,
            json=payload
        )

        return response.json()
        
    async def upload_images(self, images:list, return_object:bool=True) -> dict:
        params = {"returnInObject": return_object}
        files = [
            ('images', (image, open(image, 'rb'), 'image/png'))
            for image in images
        ]
    
        response = await send_and_parse(
            method="POST",
            url=self.endpoint["upload_images"],
            headers=self.headers,
            params=params,
            files=files
        )
        return response.json()
        
    async def training_model(self) -> dict:
        response = await send_and_parse(
            method="POST",
            url=self.endpoint["training"],
            headers=self.headers,
        )
        return response.json()
        
    async def generate_image(
        self, prompt:str, steps:int=150, width:int=720,
        height:int=720, number_images:int=4, prompt_strength:int=20,
        seed:int=4523184, restore_faces:bool=True, enhance_prompt:bool=True,
        negative_prompt:str=None
    ) -> dict:
        payload = {
            "prompt": prompt,
            "steps": steps,
            "width": width,
            "height": height,
            "numberOfImages": number_images,
            "promptStrength": prompt_strength,
            "seed": seed,
            "restoreFaces": restore_faces,
            "enhancePrompt": enhance_prompt,
            "negativePrompt": negative_prompt,
        }
        
        response = await send_and_parse(
            method="POST",
            url=self.endpoint["generate_image"],
            headers=self.headers,
            json=payload
        )
        return response.json()

    async def output_images(self, only_finished:bool=True) -> dict:
        response =  await send_and_parse(
            method="GET",
            url=self.endpoint["output_images"],
            headers=self.headers,
            params={"onlyFinished": only_finished}
        )
        return response.json()
        
    async def output_image(self, inference_id:str) -> dict:
        response =  await send_and_parse(
            method="GET",
            url=self.endpoint["output_image"].format(inference_id=inference_id),
            headers=self.headers,
        )
        return response.json()
        