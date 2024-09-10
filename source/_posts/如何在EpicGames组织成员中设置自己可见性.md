---
title: 如何在大型组织中设置自己成员可见性
date: 2024-09-10 17:04:12
tags:
---



# 问题的提出
我加入了`EpicGames`组织，但中的member数量过于多，通过[传统方法](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-membership-in-organizations/publicizing-or-hiding-organization-membership)设置自己的可见性是行不通的，因为github的服务器最多返回50K条数据，利用搜索功能也是搜不到的。
<!--more-->

# 问题的分析
如果不能通过github网页版解决，那么是否可以通过github api解决。

通过搜索github docs，我找到了这个API（参考资料2），可以设置自己在org里面的可见性。

# 问题的解决
我发现通过GitHub CLI工具调用这个API是最简单的。首先需要安装GitHub CLI（参考资料3）。

安装完成后登录
```shell
gh auth login
```

登陆以后按照API文档中的示例进行调用

```shell
gh api   --method PUT   -H "Accept: application/vnd.github+json"   -H "X-GitHub-Api-Version: 2022-11-28"   /orgs/{组织名称}/public_members/{用户名称}
```

完工


# 参考资料
1. [GitHub REST API 快速入门](https://docs.github.com/zh/rest/quickstart?apiVersion=2022-11-28)
2. [Set public organization membership for the authenticated user](https://docs.github.com/zh/rest/orgs/members?apiVersion=2022-11-28#set-public-organization-membership-for-the-authenticated-user)
3. [安装github CLI](https://github.com/cli/cli?tab=readme-ov-file#windows)