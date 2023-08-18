from ray.job_submission import JobSubmissionClient

# If using a remote cluster, replace 127.0.0.1 with the head node's IP address.
client = JobSubmissionClient("http://127.0.0.1:8265")
job_id = client.submit_job(
    # Entrypoint shell command to execute
    entrypoint="chmod +x ./run_llama_ft.sh && ./run_llama_ft.sh --size=7b",
    # Path to the local directory that contains the script.py file
    runtime_env={
        "working_dir": "./",
        "env_vars": {
                "HF_HOME": "~/.cache/huggingface",
                "TUNE_RESULT_DIR": "/tmp/output",
        },
        "pip": ["--index-url https://pypi.tuna.tsinghua.edu.cn/simple", "datasets", "evaluate", "fsspec", "s3fs", ]
    }
)
print(job_id)