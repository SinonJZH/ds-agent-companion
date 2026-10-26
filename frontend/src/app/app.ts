// SPDX-License-Identifier: AGPL-3.0-or-later
// Copyright (C) 2026 SinonJZH

import {Component, signal} from '@angular/core';
import {RouterOutlet} from '@angular/router';

@Component({
  imports: [RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.scss',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('frontend');
}
