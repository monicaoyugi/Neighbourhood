import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';
import { Hood } from './hood.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  hoods$: Hood[];

  constructor(private dataService: DataService) {}

  ngOnInit() {
    return this.dataService.getHoods()
      .subscribe(data => this.hoods$ = data)
  }

  title = 'Neighbourhood';
}
