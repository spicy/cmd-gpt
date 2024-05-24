from config.settings import MAX_LINES_PER_CHUNK
from core.interfaces import IChunkService

class ChunkService(IChunkService):
    def chunk_content(self, content, label="Original"):
        lines = content.split('\n')
        chunks = ['\n'.join(lines[i:i + MAX_LINES_PER_CHUNK]) for i in range(0, len(lines), MAX_LINES_PER_CHUNK)]
        labels = [label] * len(chunks)
        return chunks, labels