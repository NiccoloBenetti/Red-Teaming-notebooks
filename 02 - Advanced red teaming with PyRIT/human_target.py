from pyrit.prompt_target import PromptTarget
from pyrit.models import PromptRequestResponse, PromptRequestPiece, construct_response_from_request
import asyncio

class ManualHumanTarget(PromptTarget):
    name = "ManualHuman"

    async def send_prompt_async(self, *, prompt_request: PromptRequestResponse) -> PromptRequestResponse:
        self._validate_request(prompt_request)

        request = prompt_request.request_pieces[0]
        print(f"\n🧠 Adversarial prompt:\n{request.converted_value}")
        response_text = input("🧙🏻 Write here the Gandalf's response:\n> ").strip()

        return construct_response_from_request(request=request, response_text_pieces=[response_text])

    def _validate_request(self, prompt_request: PromptRequestResponse) -> None:
        if len(prompt_request.request_pieces) != 1:
            raise ValueError("You can only insert one prompt at a time.")

        if prompt_request.request_pieces[0].converted_value_data_type != "text":
            raise ValueError("Only text prompts are supported.")
