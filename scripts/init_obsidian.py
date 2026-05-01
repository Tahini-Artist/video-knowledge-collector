#!/usr/bin/env python3
"""
初始化 Obsidian 视频知识库目录结构

用法：
    python init_obsidian.py <obsidian_path>

示例：
    python init_obsidian.py /Users/mingyuewu/Documents/Obsidian/我的知识库
"""

import os
import sys
from pathlib import Path


def create_obsidian_structure(base_path: str):
    """创建 Obsidian 视频知识库目录结构"""
    
    base = Path(base_path)
    
    if not base.exists():
        print(f"❌ 路径不存在：{base_path}")
        return False
    
    # 目录结构
    directories = [
        "00-收件箱",
        "01-视频素材/流量获取",
        "01-视频素材/产品开发",
        "01-视频素材/变现方法",
        "01-视频素材/内容创作",
        "01-视频素材/用户运营",
        "01-视频素材/工具效率",
        "01-视频素材/思维认知",
        "01-视频素材/其他",
        "02-行动清单",
        "03-知识网络",
        "04-模板",
    ]
    
    created = []
    for dir_path in directories:
        full_path = base / dir_path
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            created.append(dir_path)
    
    # 创建 README
    readme_path = base / "00-收件箱" / "README.md"
    if not readme_path.exists():
        readme_path.write_text("""# 收件箱

新收集的视频素材会先放在这里，分类后再移动到对应主题文件夹。

## 使用说明

1. 新视频笔记保存在此文件夹
2. 确认主题分类后，移动到 `01-视频素材/{主题}/` 文件夹
3. 使用 Obsidian 的双链功能关联相关笔记
""")
        created.append("00-收件箱/README.md")
    
    # 创建行动清单模板
    action_path = base / "02-行动清单" / "待办汇总.md"
    if not action_path.exists():
        action_path.write_text("""# 待办汇总

所有从视频中提取的行动建议汇总在此。

---

## 📌 立即执行（今天）

- [ ] 

---

## 📅 短期计划（本周）

- [ ] 

---

## 🎯 长期探索（持续）

- [ ] 

---

最后更新：{{date}}
""")
        created.append("02-行动清单/待办汇总.md")
    
    if created:
        print(f"✅ 已创建 {len(created)} 个目录/文件：")
        for item in created:
            print(f"   - {item}")
    else:
        print("✅ 目录结构已存在，无需创建")
    
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python init_obsidian.py <obsidian_path>")
        print("示例：python init_obsidian.py /Users/mingyuewu/Documents/Obsidian/我的知识库")
        sys.exit(1)
    
    obsidian_path = sys.argv[1]
    create_obsidian_structure(obsidian_path)
