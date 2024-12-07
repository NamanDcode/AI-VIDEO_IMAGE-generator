from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GeneratedContent(Base):
    __tablename__ = 'generated_content'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)  # 'image' or 'video'
    prompt = Column(String, nullable=False)
    content_url = Column(String, nullable=False)  # URL for image or video file path

    def __repr__(self):
        return f"<GeneratedContent(type={self.type}, prompt={self.prompt}, content_url={self.content_url})>"
