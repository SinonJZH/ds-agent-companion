// SPDX-License-Identifier: AGPL-3.0-or-later
// Copyright (C) 2026 SinonJZH

import {bootstrapApplication} from '@angular/platform-browser';
import {appConfig} from './app/app.config';
import {App} from './app/app';

bootstrapApplication(App, appConfig)
  .catch((err) => console.error(err));
