---
date: '2026-11-21'
description: https://vitepress.dev/
---

# VitePress

Vite と Vue をベースにした静的サイトジェネレータ。Markdown でドキュメントサイトを作る。

- Documentation: https://vitepress.dev/
- Source: https://github.com/vuejs/vitepress

以下は、VitePress 1.6.4 時点の情報。リポジトリ(Git で管理しているドキュメント群)のルートを対象にして、ローカルの開発サーバーで閲覧する用途を想定している。

## Getting Started

Node.js が要る。バージョン管理には、[nodenv](../../program/js/node/index.md#nodenv) などが使える。

```sh
echo 24.22.3 > .node-version    # nodenv でバージョンを固定する
npm init -y
npm install -D vitepress
```

`package.json` に、スクリプトを足す。

```json
{
  "private": true,
  "scripts": {
    "docs:dev": "vitepress dev",
    "docs:build": "vitepress build",
    "docs:preview": "vitepress preview"
  },
  "devDependencies": {
    "vitepress": "^1.6.4"
  }
}
```

```sh
npm run docs:dev      # 開発サーバー(http://localhost:5173/)
```

- 設定ファイルは `.vitepress/config.mts`(`.js`、`.ts` などでもよい)。
- `.gitignore` に、`node_modules`、`.vitepress/cache`、`.vitepress/dist` を足す。

## 設定

設定は `.vitepress/config.mts` に、`defineConfig` で書く。リファレンス: https://vitepress.dev/reference/site-config

```ts
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'My Docs',
  lang: 'ja',
  // 以下、個別の設定
})
```

### srcDir、srcExclude、rewrites

Markdown を探す範囲と、URL との対応を決める設定。

| 設定 | 既定 | 内容 |
| :--- | :--- | :--- |
| `srcDir` | `.` | Markdown を探す起点。設定ファイルのあるプロジェクトルートからの相対 |
| `srcExclude` | なし | 対象外にするファイル(glob) |
| `rewrites` | なし | ソースのパスと、公開するパスの対応 |

```ts
export default defineConfig({
  srcDir: './docs',                          // docs/ 以下を対象にする
  srcExclude: ['tmp/**', '**/drafts/**'],    // 作業用のファイルを除く
  rewrites: {
    'README.md': 'index.md',                 // README.md をトップページにする
  },
})
```

- `srcDir: '.'` なら、プロジェクトルート全体が対象になる。`docs/` の外の Markdown(`README.md` など)も閲覧できる。
- ルート全体を対象にするときは、トップページ(`index.md`)がなければ、`rewrites` で `README.md` を割り当てる。
- 他のディレクトリへのシンボリックリンクがあると、同じ内容が二重に出る。`srcExclude` で除外する。

### markdown

Markdown のパーサ(markdown-it)の設定。

```ts
export default defineConfig({
  markdown: {
    attrs: { disable: true },
    config: (md) => {
      // markdown-it のインスタンスに、プラグインやルールを足す
    },
  },
})
```

#### attrs

VitePress は、markdown-it-attrs を有効にしていて、ブロックの末尾の `{...}` を属性指定として解釈する(例: `## 見出し {#my-id}`)。

- `{プレースホルダ}` だけの行を含むテンプレートの文書は、ビルドエラーになる。
- `markdown.attrs.disable: true` で、この解釈を無効にする。

#### `{{ }}` と v-pre

Markdown は Vue のテンプレートにコンパイルされるので、`{{ ... }}` は Vue の式として解釈される。
Hugo のショートコード(`{{< ref "..." >}}`)の説明のように、`{{ }}` を含む文書は、ビルドエラーになることがある。

- コードブロック(フェンス)には、`v-pre` が付くので、問題ない。
- インラインコードは、文脈によってはエラーになる(表のセルの中など)。`markdown.config` で、`v-pre` を付ける。
- コードの外の本文に書くと、エラーになる。コードで囲む。

```ts
markdown: {
  config: (md) => {
    const defaultRender = md.renderer.rules.code_inline!
    md.renderer.rules.code_inline = (tokens, idx, options, env, self) =>
      defaultRender(tokens, idx, options, env, self).replace('<code', '<code v-pre')
  },
},
```

- 個別の文書では、ブロックを `::: v-pre` ... `:::` で囲む方法もある。

### ignoreDeadLinks

| 設定 | 既定 | 内容 |
| :--- | :--- | :--- |
| `ignoreDeadLinks` | `false` | リンク切れを、ビルドエラーにするか |

- `true` にすると、エラーにしない。対象外のファイルや他のリポジトリを指す相対リンクがある場合に使う。
- 特定のリンクだけ除外するには、文字列、正規表現、関数の配列を渡す。

### vite

`vite` に、Vite の設定をそのまま渡せる。

```ts
export default defineConfig({
  vite: {
    server: {
      watch: {
        ignored: ['**/.git/**', '**/node_modules/**', '**/.vitepress/cache/**', '**/.vitepress/dist/**'],
      },
    },
  },
})
```

- `server.watch.ignored` ... 開発サーバーのファイル監視から外すパス。`srcDir` を広く取ると、監視が `.git/` や `node_modules/` に及んで、高負荷になることがある。
- `plugins` ... Vite のプラグインを足せる(下記「Markdown の追加・削除を反映する」)。

### themeConfig

既定テーマの設定。

| 設定 | 内容 |
| :--- | :--- |
| `sidebar` | サイドバーの項目。既定は、なし(自動では作られない) |
| `nav` | ヘッダーのナビゲーション |
| `outline` | 右側の目次の設定(例: `{ level: [2, 3] }`) |

## サイドバーの自動生成

VitePress は、サイドバーを自動では作らない。`themeConfig.sidebar` に、項目を明記する。
項目を、ディレクトリの階層から作る関数の例。設定ファイルの中(または別ファイル)に書く。

```ts
import fs from 'node:fs'
import path from 'node:path'
import type { DefaultTheme } from 'vitepress'

const root = path.resolve(__dirname, '..')

// 最初の # 見出しを、項目名にする
function titleOf(file: string, fallback: string): string {
  const src = fs.readFileSync(file, 'utf8')
  const body = src.replace(/^---\n[\s\S]*?\n---\n/, '') // frontmatter を除く
  const h1 = body.match(/^#\s+(.+)$/m)
  return h1 ? h1[1].trim() : fallback
}

function scan(dir: string): DefaultTheme.SidebarItem[] {
  const entries = fs.readdirSync(path.join(root, dir), { withFileTypes: true })
    .sort((a, b) => a.name.localeCompare(b.name))
  const items: DefaultTheme.SidebarItem[] = []
  for (const e of entries) {
    const rel = path.posix.join(dir, e.name)
    if (e.isDirectory()) {
      const children = scan(rel)
      if (children.length > 0) items.push({ text: e.name, collapsed: true, items: children })
    } else if (e.name.endsWith('.md') && e.name !== 'index.md') {
      items.push({ text: titleOf(path.join(root, rel), e.name), link: `/${rel.replace(/\.md$/, '')}` })
    }
  }
  return items
}
```

- `__dirname` は、設定ファイルの読み込み時に VitePress(Vite)が置き換えるので、`.mts` でも使える。
- 項目名は、frontmatter の `title` ではなく、最初の `#` 見出しから取る。

### Markdown の追加・削除を反映する

`themeConfig.sidebar` は、設定の読み込み時(サーバーの起動時)に1回だけ評価される。このため、Markdown を追加・削除しても、サーバーを再起動するまで反映されない。
Vite のプラグインで、追加・削除を検知したら、設定ファイルを touch すると、反映できる。VitePress は設定ファイルの変更を検知して、設定を再読み込みする。

```ts
import fs from 'node:fs'

export default defineConfig({
  vite: {
    plugins: [
      {
        name: 'reload-sidebar-on-add-unlink',
        configureServer(server) {
          let timer: NodeJS.Timeout | undefined
          const touch = (file: string) => {
            if (!file.endsWith('.md')) return
            clearTimeout(timer)
            timer = setTimeout(() => {
              const now = new Date()
              fs.utimesSync(__filename, now, now)
            }, 300)
          }
          server.watcher.on('add', touch)
          server.watcher.on('unlink', touch)
        },
      },
    ],
  },
})
```

- 反映には数秒かかる。ブラウザのリロードも要る。
- 見出しだけを変えた場合は、検知しない。

## 動作のメモ

- ドットで始まるディレクトリ(`.claude/` など)の Markdown は、`vitepress build` の出力に含まれない。開発サーバーでは、パスを指定すれば開ける。
- `npx vitepress --version` は、バージョンを表示せず、開発サーバーを起動する(1.6.4 時点)。バージョンは `package.json` か `npm ls vitepress` で確認する。
- `npm install` で、esbuild の postinstall が `allowScripts` の対象外だという警告が出ることがある(npm 11)。動作には影響しなかった。

## 参考

- https://vitepress.dev/guide/getting-started
- https://vitepress.dev/reference/site-config
