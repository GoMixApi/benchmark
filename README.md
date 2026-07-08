# GoMixApi Benchmark

Daily AI model performance comparison across code generation, translation, and long-context summarization. Data is automatically generated and updated daily at 03:00 UTC+8.

## Latest Results

*(Auto-updated daily from our Benchmark script)*

### 2026-07-08

| Model | Code Generation | Translation | Long Context Summary |
|-------|:--:|:--:|:--:|
| **DeepSeek V4 Flash** | ✅ 3.96s | ✅ 2.66s | ✅ 2.07s |
| **Qwen3.7-Plus** | ✅ 24.3s | ✅ 9.1s | ✅ 33.4s |
| **Dola Seed-2.0-Lite** | ✅ 18.8s | ✅ 10.3s | ✅ 6.2s |

*Full JSON data available in the `/data` directory.*

## Models Tested

- DeepSeek V4 Flash (`deepseek-v4-flash-202605`)
- Qwen3.7-Plus (`qwen3.7-plus`)
- Dola Seed-2.0-Lite (`dola-Seed-2.0-lite`)

## Test Categories

| Test | Description | Scoring |
|------|-------------|---------|
| Code Generation | Write Fibonacci function in Python | Success + Latency |
| Translation | English → Chinese (tech context) | Success + Latency |
| Long Context Summary | Summarize a complex description | Success + Latency |

## How It Works

1. Script runs daily at 03:00 UTC+8
2. Calls GoMixApi endpoints for 3 models × 3 tests
3. Outputs structured JSON to `/data/benchmark_YYYYMMDD.json`
4. Also updates `/data/latest.json` with the most recent results
5. Data powers our [Status Page](https://gomixapi.com/status) and [Blog](https://gomixapi.com/blog)

## Related Projects

- [GoMixApi Integrations](https://github.com/GoMixApi/integrations) — Dify, LangChain, OpenWebUI templates
- [GoMixApi Status](https://gomixapi.com/status) — Live API health dashboard
- [GoMixApi Pricing](https://gomixapi.com/pricing) — Transparent model pricing
