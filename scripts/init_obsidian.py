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
from datetime import datetime


def create_obsidian_structure(base_path: str):
    """创建 Obsidian 视频知识库目录结构"""
    
    base = Path(base_path)
    
    # 如果路径不存在，询问是否创建
    if not base.exists():
        print(f"⚠️  路径不存在：{base_path}")
        print(f"是否创建该目录？(y/n): ", end="")
        response = input().strip().lower()
        if response == 'y':
            base.mkdir(parents=True, exist_ok=True)
            print(f"✅ 已创建目录：{base_path}")
        else:
            print("❌ 已取消")
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

---

## 📂 目录结构说明

| 文件夹 | 用途 |
|--------|------|
| 00-收件箱 | 新收集的视频 |
| 01-视频素材 | 按主题分类的视频笔记 |
| 02-行动清单 | 待办汇总 |
| 03-知识网络 | 主题关系图 |
| 04-模板 | 模板文件 |

---

创建时间：{date}
""".format(date=datetime.now().strftime("%Y-%m-%d")))
        created.append("00-收件箱/README.md")
    
    # 创建行动清单模板
    action_path = base / "02-行动清单" / "本周待办.md"
    if not action_path.exists():
        action_path.write_text("""# 本周待办

> 所有从视频中提取的行动建议汇总在此
> 最后更新：{date}

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

## 待办来源

| 视频 | 来源 | 收集时间 |
|------|------|----------|
| | | |

---

#待办 #行动清单
""".format(date=datetime.now().strftime("%Y-%m-%d")))
        created.append("02-行动清单/本周待办.md")
    
    # 创建视频笔记模板
    template_path = base / "04-模板" / "视频笔记模板.md"
    if not template_path.exists():
        template_path.write_text("""---
title: {{视频标题}}
source: {{小红书/抖音/B站}}
url: {{视频链接}}
author: {{博主名称}}
collected: {{收集时间}}
topic: {{主题分类}}
duration: {{视频时长}}
tags:
  - 视频素材
  - {{平台}}
  - {{主题}}
---

# {{视频标题}}

## 📌 基本信息

| 项目 | 内容 |
|------|------|
| 来源 | {{平台}} |
| 博主 | {{博主}} |
| 链接 | {{URL}} |
| 时长 | {{视频时长}} |
| 收集时间 | {{日期}} |
| 主题分类 | {{主题}} |

---

## 💡 完整知识点

> 提取视频中的所有知识点，不做精简

### 一、{{核心主题 1}}

#### 1.1 {{知识点标题}}

- **核心概念**：...
- **具体方法**：...
- **实际案例**：...
- **适用场景**：...
- **时间点**：[00:00]

---

## ✅ 个性化行动建议

> 基于你的身份【{{用户身份}}】、业务【{{用户业务}}】、目标【{{用户目标}}】生成

### 📌 立即执行（今天可做）

#### 行动 1：{{具体行动}}

- **做什么**：{{具体操作步骤}}
- **为什么**：{{与你的目标的关系}}
- **预期效果**：{{预计能带来什么}}
- **所需时间**：{{预估时间}}

---

## 🔗 相关素材

### 同主题
- [[相关视频1]]
- [[相关视频2]]

---

## 📝 原始摘录

> 视频原文的重要内容摘录，保留原始表述

---

#视频素材 #{{平台}} #{{主题}}
""")
        created.append("04-模板/视频笔记模板.md")
    
    if created:
        print(f"\n✅ 已创建 {len(created)} 个目录/文件：")
        for item in created:
            print(f"   - {item}")
    else:
        print("\n✅ 目录结构已存在，无需创建")
    
    print(f"\n📁 Obsidian 知识库路径：{base_path}")
    print("\n🎉 初始化完成！现在可以发送视频链接开始分析了。")
    
    return True


def check_obsidian_path(base_path: str) -> bool:
    """检查 Obsidian 路径是否有效"""
    
    base = Path(base_path)
    
    if not base.exists():
        return False
    
    # 检查是否包含 .obsidian 文件夹（Obsidian 仓库标识）
    obsidian_folder = base / ".obsidian"
    if obsidian_folder.exists():
        print(f"✅ 检测到 Obsidian 库：{base_path}")
        return True
    
    print(f"⚠️  路径存在但未检测到 .obsidian 文件夹")
    print(f"   这可能不是一个 Obsidian 库，但仍可使用")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python init_obsidian.py <obsidian_path>")
        print("示例：python init_obsidian.py /Users/mingyuewu/Documents/Obsidian/我的知识库")
        sys.exit(1)
    
    obsidian_path = sys.argv[1]
    print(f"\n🔍 检查路径：{obsidian_path}")
    check_obsidian_path(obsidian_path)
    create_obsidian_structure(obsidian_path)
