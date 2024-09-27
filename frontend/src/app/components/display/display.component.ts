import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { StudentService } from '../../services/student.service';

@Component({
  selector: 'app-display',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './display.component.html',
  styleUrl: './display.component.css'
})
export class DisplayComponent implements OnInit {

  constructor(private studentService: StudentService) { }

  students: any[] = []

  ngOnInit() {
    this.studentService.getStudents().subscribe((data: any) => {
      this.students = data;
    });
  }

}
