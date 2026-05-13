#!/bin/bash
# ============================================================
# 멋쟁이사자처럼 Owned Media 프로젝트 — 폴더 세팅 스크립트
# 실행: bash setup.sh
# 최초 1회만 실행
# ============================================================

PROJECT="likelion-owned-media"

echo "📁 프로젝트 폴더 생성 중: $PROJECT"

mkdir -p "$PROJECT/00_overview"
mkdir -p "$PROJECT/01_strategy/channel-policy"
mkdir -p "$PROJECT/02_content/drafts"
mkdir -p "$PROJECT/03_crm"
mkdir -p "$PROJECT/04_research/user-research"
mkdir -p "$PROJECT/05_reports"
mkdir -p "$PROJECT/scripts"
mkdir -p "$PROJECT/.claude/commands"

echo "📄 .gitkeep 파일 생성 중 (빈 폴더 Git 추적용)"
find "$PROJECT" -type d -empty -exec touch {}/.gitkeep \;

echo ""
echo "✅ 세팅 완료! 폴더 구조:"
find "$PROJECT" -type d | sed 's|[^/]*/|  |g'

echo ""
echo "👉 다음 단계:"
echo "   1. CLAUDE.md, README.md, .claude/commands/*.md 파일을 복사해서 붙여넣으세요"
echo "   2. VSCode에서 'code $PROJECT' 로 열기"
echo "   3. Claude Code 실행 후 세션 시작 문구 사용"
