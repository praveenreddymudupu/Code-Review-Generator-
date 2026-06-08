from langfuse_config import langfuse

obs = langfuse.start_as_current_observation(
    name="manual-test"
)

print("Observation created")

langfuse.flush()

print("Flushed")