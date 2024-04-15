import { Component, OnInit,Input} from '@angular/core';
import { SharedService } from 'src/app/shared.service';
import { GroupSort } from 'src/assets/group.model';


@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit  {

  constructor(private service:SharedService) {}

  @Input('gName') groupM!: GroupSort;



  ngOnInit(): void {

    this.service.msgAlert('warning','Attention !!',"The Draft was completed on 06/12/2023 However, you can keep using this simulator");
  }

}
