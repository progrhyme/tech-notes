---
title: "CronJob"
linkTitle: "CronJob"
date: 2021-03-04T09:12:03+09:00
weight: 80
---

繰り返し実行されるジョブ。  
Cron形式でスケジュールの記述が可能。

## Documentation

- [CronJob | Kubernetes](https://kubernetes.io/ja/docs/concepts/workloads/controllers/cron-jobs/)
- [Running Automated Tasks with a CronJob | Kubernetes](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/)
- [APIリファレンス v1beta1](https://kubernetes.io/docs/reference/kubernetes-api/workloads-resources/cron-job-v1beta1/)
- [APIリファレンス v2alpha1](https://kubernetes.io/docs/reference/kubernetes-api/workloads-resources/cron-job-v2alpha1/)

## Spec

 Field | Data Type | Description
-------|-----------|-------------
 startingDeadlineSeconds | int64 | オプショナル。ジョブが開始するまでの期限を秒数で表す。スケジュール通りに実行されなかったジョブは失敗として数えられる
