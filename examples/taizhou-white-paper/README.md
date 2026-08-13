# TAIZHOU 品牌企业白皮书案例

这是 `aos-agent-skill-document` 的公开、可重复生成案例。案例采用 TAIZHOU 企业系统，以及 WANMIAN / 万棉尚品、GEERNA / 哥尔纳、UIUP 三品牌架构。

所有经营数字、价格带、组织职责和增长目标均为 `PLANNING ASSUMPTION / 企划模拟值`，不能当作已验证企业事实。

## 生成案例

在仓库根目录执行一键发布构建：

```bash
python examples/taizhou-white-paper/build_release.py \
  --output-dir examples/taizhou-white-paper/output \
  --qa-dir /tmp/taizhou-example-qa
```

该命令会依次生成 DOCX、应用高清图片设置、清理个人元数据、渲染全部页面、导出并清理 PDF 元数据、再次渲染 PDF，以及生成联系表。

如果只需要生成未发布处理的源 DOCX：

```bash
python examples/taizhou-white-paper/generate_example.py \
  --brief examples/taizhou-white-paper/brief.json \
  --output /tmp/TAIZHOU-source.docx
```

## 已提交输出

- `output/TAIZHOU品牌企业白皮书_示例版.docx`
- `output/TAIZHOU品牌企业白皮书_示例版.pdf`
- `output/TAIZHOU品牌企业白皮书_示例版_联系表.jpg`

案例内容按 CC BY 4.0 开放，商标权不在授权范围内。
