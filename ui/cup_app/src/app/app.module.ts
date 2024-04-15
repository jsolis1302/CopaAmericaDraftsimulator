import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { GroupComponent } from './group/group.component';
import { HeaderComponent } from './header/header.component';
import { HttpClientModule } from "@angular/common/http";
import { SharedService } from './shared.service';
import { CountryComponent } from './country/country.component';
import { AppRoutingModule } from './app-routing.module';
import { DrafComponent } from './draf/draf.component';
import { TournamentComponent } from './tournament/tournament.component';
import { FormsModule } from '@angular/forms';
import { SelectCountryComponent } from './select-country/select-country.component';

@NgModule({
  declarations: [
    AppComponent,
    GroupComponent,
    HeaderComponent,
    CountryComponent,
    DrafComponent,
    TournamentComponent,
    SelectCountryComponent
    
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
