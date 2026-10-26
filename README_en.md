# ds-agent-companion

English | [简体中文](README.md)

A local, single-user AI roleplay companion powered by the DeepSeek API: the model plays a character with long-term
memory and a schedule of its own, reaching out to chat or post on its own initiative. The engine runs locally and serves
desktop, mobile browser, and headless clients.

> **Status**: The project is in the design phase — architecture and UI design are finalized; no code has been written
> yet.

## Planned Features

- **Long-term memory**: four-layer rolling notes + vector store + state cards, with public/private partitioned injection
  and append-only storage.
- **Proactive companionship**: a scheduler layer handles time/condition-based triggers; the character initiates private
  chats and posts to an SNS timeline.
- **Persona packages**: persona, worldview, personality pool, and origin memories bundled as importable/exportable
  directory packages.
- **Multi-client access**: a single engine process serving multiple frontends (pywebview desktop shell, mobile browser /
  PWA, headless deployment).

## Tech Stack

Python (asyncio) · DeepSeek API · SQLite (sqlite-vec) · fastembed · Angular · ConnectRPC

## Documentation

- [Architecture](doc/ARCHITECTURE.md) (Chinese)
- [UI Design](doc/ui_design.md) (Chinese)
- [Testing](doc/testing.md) (Chinese)
- [Document Revisions](doc/revisions.md) (Chinese)

## License

This project is licensed under [AGPL-3.0](LICENSE).
