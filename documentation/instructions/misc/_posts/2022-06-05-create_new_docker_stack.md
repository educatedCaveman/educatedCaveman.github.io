---
title: Create a New Docker Stack
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

steps 2-4 will have to be performed separately for the `dev_test` and `master` branches.

1. Follow all the instructions for creating a new GitHub repository, [here]({% post_url /documentation/instructions/misc/2022-06-05-create_new_git_repo %})
2. Portainter setup:
   - add new stack
     - github type
     - populate main github URL
     - populate ref:
       - `refs/heads/master`
       - `refs/heads/dev_test`
     - update compose file path, if needed. (typically it wont be)
     - auto-update, using a webhook
   - copy the webhook
3. Jenkins setup
   - add the webhook as secret text to the credentials manager
4. Repository setup
   - update the Jenkinsfile with the appropriate webhook names
   - perform whatever code setup the docker stack requires
5. If necessary or desired, follow the documented steps for creating an SSL endpoint for the service.
