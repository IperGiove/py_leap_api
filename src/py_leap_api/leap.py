from utils import send_and_parse

class TryLeap:
    
    def __init__(self, api: str, model: str=None) -> None:
        self.api = api
        self.model = model
    
    async def create_model(self, title:str, subject:str="@me", identifier:str=None) -> dict:
        payload = {
            "title": title,
            "subjectKeyword": subject,
            "subjectIdentifier": identifier
            }
        
        response = await send_and_parse(
            method="POST",
            url=cfg.endpoint.create_model,
            headers=cfg.headers,
            json=payload
        )
        
        return response.json()
        
    async def upload_images_url(self, images:list, return_object:bool=True) -> dict:
        params = {"returnInObject": return_object}
        payload = {"images": images}
    
        response = await send_and_parse(
            method="POST",
            url=cfg.endpoint.upload_images,
            headers=cfg.headers,
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
            url=cfg.endpoint.upload_images,
            headers=cfg.headers,
            params=params,
            files=files
        )
        return response.json()
        
    async def training_model(self) -> dict:
        response = await send_and_parse(
            method="POST",
            url=cfg.endpoint.training,
            headers=cfg.headers,
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
            url=cfg.endpoint.generate_image,
            headers=cfg.headers,
            json=payload
        )
        return response.json()

    async def output_images(self, only_finished:bool=True) -> dict:
        response =  await send_and_parse(
            method="GET",
            url=cfg.endpoint.output_images,
            headers=cfg.headers,
            params={"onlyFinished": only_finished}
        )
        return response.json()
        
    async def output_image(self, image_id:str) -> dict:
        response =  await send_and_parse(
            method="GET",
            url=cfg.endpoint.output_images,
            headers=cfg.headers,
            params={"inferenceId": image_id}
        )
        return response.json()
        