package com.jobconnect.backend.controller;

import com.jobconnect.backend.entity.Job;
import com.jobconnect.backend.repository.JobRepository;
import com.jobconnect.backend.security.CustomUserDetails;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/recruiter/jobs")
@PreAuthorize("hasAuthority('ROLE_RECRUITER')")
public class RecruiterJobController {

    @Autowired
    private JobRepository jobRepository;

    @GetMapping
    public ResponseEntity<List<Job>> getMyPostedJobs() {
        CustomUserDetails userDetails = (CustomUserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        return ResponseEntity.ok(jobRepository.findByRecruiterId(userDetails.getId()));
    }

    @PostMapping
    public ResponseEntity<?> postNewJob(@RequestBody Job job) {
        CustomUserDetails userDetails = (CustomUserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        
        com.jobconnect.backend.entity.User recruiter = new com.jobconnect.backend.entity.User();
        recruiter.setId(userDetails.getId());
        job.setRecruiter(recruiter);
        job.setStatus("ACTIVE");
        
        Job savedJob = jobRepository.save(job);
        return ResponseEntity.ok(savedJob);
    }
}
