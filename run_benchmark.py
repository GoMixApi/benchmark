#!/usr/bin/env python3
import json, time, os
from datetime import datetime
from openai import OpenAI

API_KEY = 'sk-9tBhsoPbftLkbPCyxmHp02SFVqflTwJ5OivufA00PicIppAN'
BASE_URL = 'https://api.gomixapi.com/v1'
OUTPUT_DIR = '/opt/gomixapi-benchmark/data'

MODELS = ['deepseek-v4-flash-202605', 'qwen3.7-plus', 'dola-Seed-2.0-lite']

TESTS = {
    'code_generation': {
        'prompt': 'Write a Python function to calculate the Fibonacci sequence up to n terms.',
        'max_tokens': 200
    },
    'translation': {
        'prompt': "Translate this to Chinese: 'Artificial intelligence is transforming every industry across Southeast Asia.'",
        'max_tokens': 100
    },
    'long_context_summary': {
        'prompt': (
            'Summarize in one sentence: '
            'GoMixAPI is an enterprise-ready AI gateway for Southeast Asia, offering 17 curated models '
            '(DeepSeek, Qwen, GLM, Hunyuan, Dola) through one OpenAI-compatible endpoint. '
            'Operated by YiMay Technology Limited, a Hong Kong-licensed entity, with zero data retention, '
            'SCC 2021/914, DPA ready, and unified billing.'
        ),
        'max_tokens': 80
    }
}

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def run_test(model, test_name, test_config):
    start = time.time()
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{'role': 'user', 'content': test_config['prompt']}],
            max_tokens=test_config['max_tokens'],
            temperature=0.0
        )
        elapsed = round(time.time() - start, 2)
        out = resp.choices[0].message.content
        return {
            'success': True,
            'time_seconds': elapsed,
            'output_length': len(out),
            'output_preview': out[:100] + ('...' if len(out) > 100 else '')
        }
    except Exception as e:
        return {
            'success': False,
            'time_seconds': round(time.time() - start, 2),
            'error': str(e)[:200]
        }

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = {
        'timestamp': datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00'),
        'models': {}
    }
    for model in MODELS:
        results['models'][model] = {}
        for test_name, test_config in TESTS.items():
            print(f'Testing {model} - {test_name}...')
            results['models'][model][test_name] = run_test(model, test_name, test_config)
            time.sleep(0.5)

    date_str = datetime.now().strftime('%Y%m%d')
    filepath = os.path.join(OUTPUT_DIR, f'benchmark_{date_str}.json')
    with open(filepath, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    with open(os.path.join(OUTPUT_DIR, 'latest.json'), 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    msg = f'Benchmark complete: {filepath}'
    print(msg)
    print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
