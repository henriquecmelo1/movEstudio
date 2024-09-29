import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { StudentService } from '../../services/student.service';
import { FormsModule } from '@angular/forms';
import { Ng2SearchPipe } from 'ng2-search-filter';

@Component({
  selector: 'app-display',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './display.component.html',
  styleUrl: './display.component.css'
})
export class DisplayComponent implements OnInit {

  constructor(private studentService: StudentService) { }

  students: any[] = []
  search: string = '';

  ngOnInit() {
    this.studentService.getStudents().subscribe((data: any) => {
      this.students = data;
    });
  }
  onSubmit() {
    this.studentService.filterStudents(this.search).subscribe((data: any) => {
      this.students = data;
    });
  }
  deleteStudent(id: any) {
    this.studentService.deleteStudent(id).subscribe((data: any) => {
      this.students = data;
      window.location.reload();
    });
  }

}
