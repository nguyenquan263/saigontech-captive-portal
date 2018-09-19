import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';

import { FillInfoComponent } from './fill-info/fill-info.component';
import { CheckCodeComponent } from './check-code/check-code.component';




@NgModule({
  declarations: [
    AppComponent,
    FillInfoComponent,
    CheckCodeComponent


  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    RouterModule.forRoot([
      { path: '', component: FillInfoComponent },
      { path: 'check', component: CheckCodeComponent }

    ])
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
