import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class SentenceGenerator:
    def __init__(self, model_name='gpt2-medium'):
        """
        Initialize the sentence generator with a pre-trained GPT-2 model
        """
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        # Add padding token if not exists
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate_sentences(self, prompt, num_sentences=5, max_length=100, temperature=0.7, top_k=50, top_p=0.95):
        """
        Generate similar sentences based on a given prompt
        """
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        generated_sentences = []
        
        for _ in range(num_sentences):
            output = self.model.generate(
                input_ids,
                max_length=max_length,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p,
                do_sample=True
            )
            generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
            generated_sentences.append(generated_text.split('.')[0].strip() + '.')  # Get the first sentence
        
        return generated_sentences