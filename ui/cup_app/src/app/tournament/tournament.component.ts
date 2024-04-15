import { Component } from '@angular/core';
import { Country } from 'src/assets/shared/country.model';

@Component({
  selector: 'app-tournament',
  templateUrl: './tournament.component.html',
  styleUrls: ['./tournament.component.css']
})
export class TournamentComponent {


  SF:Country[] = [];
  selectedClass:any = 0;

  QFin:Country[] = [];


  clickedSF(item:Country){
    this.SF.push(item);
  }

}
