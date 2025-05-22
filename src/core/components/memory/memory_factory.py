from src.core.components.memory.base import BaseChatbotMemory
from src.common.config import Config
from src.core.components.memory.clients.in_memory import InMemory
from src.core.components.memory.clients.mongodb_memory import MongoMemory


def create_memory(config: Config) -> BaseChatbotMemory:
    print(f"[MemoryFactory] Creating memory with type {config.bot_memory_type}")
    if config.bot_memory_type == "mongodb":
        print("[MemoryFactory] Using MongoMemory")
        return MongoMemory(config)
    elif config.bot_memory_type == "inmemory":
        print("[MemoryFactory] Using InMemory")
        return InMemory()
    else:
        raise ValueError(f"Invalid memory type: {config.bot_memory_type}")
