import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { GroupComponent } from './group/group.component';
import { CountryComponent } from './country/country.component';
import { DrafComponent } from './draf/draf.component';
import { TournamentComponent } from './tournament/tournament.component';

const routes: Routes = [
  
  { path: 'draft', component: DrafComponent },
  { path: 'countries', component: CountryComponent },
  { path: 'kophase', component: TournamentComponent },
];



@NgModule({
  declarations: [],
  imports: [
    CommonModule, RouterModule.forRoot(routes)
  ],
  exports:[RouterModule]
})
export class AppRoutingModule { 
  
}
