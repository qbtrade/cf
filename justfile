# cf justfile

# 显示所有可用命令
default:
    @just --list

# 运行测试
test:
    uv run pytest -v

# 代码检查
lint:
    uv run ruff check src/

# 代码格式化
fmt:
    uv run ruff format src/

# 类型检查
typecheck:
    uv run mypy src/cf/

# 发布 patch 版本 (0.0.x)
release-patch:
    #!/usr/bin/env bash
    set -e
    hatch version patch
    VERSION=$(hatch version)
    git add -A
    git commit -m "🔖 release: v${VERSION}"
    git tag "v${VERSION}"
    git push && git push --tags
    echo "✅ Released v${VERSION}"

# 发布 minor 版本 (0.x.0)
release-minor:
    #!/usr/bin/env bash
    set -e
    hatch version minor
    VERSION=$(hatch version)
    git add -A
    git commit -m "🔖 release: v${VERSION}"
    git tag "v${VERSION}"
    git push && git push --tags
    echo "✅ Released v${VERSION}"

# 发布 major 版本 (x.0.0)
release-major:
    #!/usr/bin/env bash
    set -e
    hatch version major
    VERSION=$(hatch version)
    git add -A
    git commit -m "🔖 release: v${VERSION}"
    git tag "v${VERSION}"
    git push && git push --tags
    echo "✅ Released v${VERSION}"
